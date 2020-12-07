/******************************************************************************
* Attribute suggestion for Citron from Tahiti (both Lemonade Project modules).
* (c) 2017 Speed Labs - Departamento de Ciência da Computação - UFMG (Brazil).
*****************************************************************************/
function caseInsensitiveComparator(a, b){
    if (! a || ! b) {
        return -1;
    } else {
        return a.toLowerCase().localeCompare(b.toLowerCase());
    }
}
var TahitiAttributeSuggester = (function () {
    var suggester = {};

    /* Private functions */
    var flatArrayOfArrays = function flatArrayOfArrays(listOfAttrs){
        return Array.prototype.concat.apply([], listOfAttrs.map(
                        function(item) {return item.attributes;}));
    };
    var cloneDeep = function(o){
      var newO
      var i

      if (typeof o !== 'object') return o

      if (!o) return o

      if (Object.prototype.toString.apply(o) === '[object Array]') {
        newO = []
        for (i = 0; i < o.length; i += 1) {
          newO[i] = cloneDeep(o[i])
        }
        return newO
      }

      newO = {}
      for (i in o) {
        if (o.hasOwnProperty(i)) {
          newO[i] = cloneDeep(o[i])
        }
      }
      return newO
    };
    /* Auxiliary */
    /**
     * general topological sort
     * @author SHIN Suzuki (shinout310@gmail.com)
     * @param Array<Array> edges : list of edges. each edge forms Array<ID,ID> e.g. [12 , 3]
     *
     * @returns Array : topological sorted list of IDs
     **/
    var topologicalSort = function(workflow){
      var topological = {info: {}}, // hash: stringified id of the task => { id: id, _targets: lisf of ids }
                      sorted = [], // sorted list of IDs ( returned value )
                      visited = {}; // hash: id of already visited task => true

      workflow.tasks.forEach(function(task){
          //task.uiPorts = {inputs: [], output: []};
          topological.info[task.id] = {targets: [], task: cloneDeep(task)};
      });
      workflow.flows.forEach(function(flow){
          if (topological.info[flow.source_id]){
              const op = topological.info[flow.target_id].task.operation;
              const target = op.ports.find(p => p.id === flow.target_port)
              topological.info[flow.source_id].targets.push(
              {
                  target: flow.target_id,
                  targetPortId: flow.target_port,
                  source: flow.source_id,
                  sourcePortId: flow.source_port,
                  order: target ? target.order : 0,
              });
          }
      });
      // 2. topological sort
      Object.keys(topological.info).forEach(function visit(taskId, ancestors) {
          var task = topological.info[taskId];

          // if already exists, do nothing
          if (visited[taskId]) return;

          if (!Array.isArray(ancestors)) ancestors = [];

          ancestors.push(taskId);

          visited[taskId] = true;
          if (task){
              task.targets.forEach(function (after) {
                  if (ancestors.indexOf(after) >= 0)  // if already in ancestors, a closed chain exists.
                      throw new Error('closed chain : ' + after.target + ' is in ' + taskId);
                  visit(after.target.toString(), ancestors.map(function (v) { return v })); // recursive call
              });
          }
          sorted.unshift(taskId);
      });
      return {order: sorted, info: topological.info};
    };
    var loadFromDataSource = function(task, result, callback) {
        if (task.uiPorts) {
            Array.prototype.push.apply(task.uiPorts.output, result);
            if (callback) {
                callback(result);
            }
        }
    }
    var onlyField = function(task, field, many) {
        if (many === undefined || !many ) {
            Array.prototype.push.apply(task.uiPorts.output,
                task.forms[field].value.split(', ').map(function(attr){return attr.trim() }));
        } else if (task.forms[field]) {
            Array.prototype.push.apply(task.uiPorts.output,
                task.forms[field].value || []);
        }
        task.uiPorts.output.sort(caseInsensitiveComparator);
    }
    var copyAddExpressionAlias = function(task, field, alias){

        task.uiPorts.output = flatArrayOfArrays(task.uiPorts.inputs);
	if (task.forms[field] && task.forms[field].value){
            var valid = (task.forms[field].value || []).filter(function(item){return item.alias});
            Array.prototype.push.apply(task.uiPorts.output,
            valid.map(function(v){return v[alias].trim()}));
        } else {
            task.uiPorts.output = [];
        }
    }
    var copyInputAddField = function(task, field, many, defaultValue){
        if (many === undefined || !many ) {
            task.uiPorts.output = flatArrayOfArrays(task.uiPorts.inputs);
            if (task.forms[field] && task.forms[field].value) {
                task.uiPorts.output.push(task.forms[field].value);
            } else if (defaultValue) {
                task.uiPorts.output.push(defaultValue);
            }
        } else {
            task.uiPorts.output = flatArrayOfArrays(task.uiPorts.inputs);
            if (task.forms[field] && task.forms[field].value.length) {
                Array.prototype.push.apply(task.uiPorts.output, task.forms[field].value);
            } else if (defaultValue) {
                task.uiPorts.output.push(defaultValue);
            }
         }
         task.uiPorts.output.sort(caseInsensitiveComparator);
    }
    var copyAllInputsRemoveDuplicated = function(task, field) {
        var attrs = flatArrayOfArrays(task.uiPorts.inputs).sort(caseInsensitiveComparator);
        if (field && task.forms[field] && task.forms[field].value){
            attrs = [];
            var newNames = task.forms[field] && task.forms[field].value.split(',');
            for(var i = 0; i < newNames.length; i++){
                attrs.push(newNames[i]);
            }
        }
        task.uiPorts.output = attrs.filter(
            function(item, index, inputArray ) {
                return inputArray.indexOf(item) === index;
             }
        );
    };
    var copyInput = function(task) {
        task.uiPorts.output = flatArrayOfArrays(task.uiPorts.inputs).sort(caseInsensitiveComparator);
    };
    var joinSuffixDuplicatedAttributes = function(task) {

        var prefix = task.forms['aliases'];
        var finalPrefix = ['ds0_', 'ds1_']
        if (prefix && prefix.value){
            var parts = prefix.value.split(',');
            if (parts.length == 2){
                finalPrefix = parts.map(function(v) { return v.trim()})
            }
        }
        var result = [];
        sorted_ports = task.uiPorts.inputs.sort(
            function(a, b) {return a.order - b.order}
        );
        if (sorted_ports.length == 2) {
            for(var p = 0; p < sorted_ports.length; p++){
                for(var i =0; i < sorted_ports[p].attributes.length; i++){
                    result.push(finalPrefix[p] + sorted_ports[p].attributes[i]);
                }
            }
            task.uiPorts.output = result.sort(caseInsensitiveComparator);
        }
    }

    var joinSuffixDuplicatedAttributes2 = function(task) {
        var parameters = task.forms['join_parameters'];
        if (! parameters){ //old parameters set
            return joinSuffixDuplicatedAttributes(task);
        }
        var value = parameters.value;
        var result = [];

        sorted_ports = task.uiPorts.inputs.sort(
            function(a, b) {return a.order - b.order}
        );
 
        if (value && sorted_ports.length == 2) {
            switch(value.firstSelectionType){
                case 1: //all attributes, with prefix
                    for(var i=0; i < sorted_ports[0].attributes.length; i++){
                        result.push(value.firstPrefix + sorted_ports[0].attributes[i]);
                    }
                    break;
                case 2:
                    value.firstSelect.filter(function(s){return s.select;})
                        .forEach(function(item){
                            result.push(item.alias || item.attribute);
                        });
                    break;
                case 3: // no attribute selected
                    break
            }
            switch(value.secondSelectionType){
                case 1: //all attributes, with prefix
                    for(var i=0; i < sorted_ports[1].attributes.length; i++){
                        result.push(value.secondPrefix + sorted_ports[1].attributes[i]);
                    }
                    break;
                case 2:
                    value.secondSelect.filter(function(s){return s.select;})
                        .forEach(function(item){
                            result.push(item.alias || item.attribute);
                        });
                    break;
                case 3: // no attribute selected
                    break;
            }
        }
        task.uiPorts.output = result.sort(caseInsensitiveComparator);
    };
    var copyInputAddAttributesSplitAlias = function(task, attributes, alias, suffix){
        task.uiPorts.output = flatArrayOfArrays(task.uiPorts.inputs);
        var aliases = [];
        if (task.forms[alias] && task.forms[alias].value){
            aliases = task.forms[alias].value.split(',').map(function(v){return v.trim()});
        } else {
            aliases = [];
        }
        if (task.forms[attributes] && task.forms[attributes].value){
            while(task.forms[attributes].value.length > aliases.length){
                var attr = task.forms[attributes].value[aliases.length];
                aliases.push(attr + suffix);
            }
        }
        Array.prototype.push.apply(task.uiPorts.output, aliases);
        task.uiPorts.output.sort(caseInsensitiveComparator);
    }
    var repeatFromAlias = function(task, alias, count) {
        var result = [];
        var aliasValue;
        if (task.forms[alias] && task.forms[alias].value){
            aliasValue = task.forms[alias].value;
        } else {
            aliasValue = 'attr_';
        }
        if (task.forms[count] && task.forms[count].value){
            var total = parseInt(task.forms[count].value);
            for (var i = 1; i <= total; i++) {
                result.push(aliasValue + '' + i)
            }
        }

        task.uiPorts.output = result;
    }
    var copyFromOnlyOneInput = function(task, id) {
        var inputs = task.uiPorts.inputs.filter(
            function(input) {
                return parseInt(input.targetPortId) === parseInt(id);
            }) || [];
        task.uiPorts.output = flatArrayOfArrays(inputs).sort(caseInsensitiveComparator);
    }
    /* Public methods */
    suggester.compute = function(workflow, dataSourceLoader, uiCallback) {

        var dataSources = [];
        workflow.tasks.forEach(function(task){
            task.uiPorts = {inputs: [], output: [], refs: []}
            var isDataSource = [18, 53, 139].includes(parseInt(task.operation.id));
            if (isDataSource) {
                dataSources.push(task);
            }
        });
        var lastStep = function() {
            var topological = topologicalSort(workflow);
            var idToSlug = {
            {%- for op, script in operations -%}
            {{op.id}}:'{{op.slug}}'{% if not loop.last %}, {% endif %}
            {%- endfor -%}
            };

            const result = {};
            topological.order.forEach(function(k){
                var task = topological.info[k].task;
                result[task.id] = task;
                switch(idToSlug[task.operation.id]){
                    {%- for op, script in operations %}
                    case '{{op.slug}}':
                        {{script.body}}
                        break;
                    {%- endfor %}
                }
                // Update next tasks' inputs with current output
                topological.info[k].targets.forEach(function(follow){
                    const newInput = Object.assign({}, follow);
                    newInput['attributes'] = task.uiPorts.output;
                    topological.info[follow.target].task.uiPorts.inputs.push(newInput);

                    // Some operations require access to attribute information
                    // from their subsequent tasks. For example, all operations
                    // that are algorithms don't have information about attributes
                    // and must query such information from model producers operations
                    topological.info[k].task.uiPorts.refs.push(topological.info[follow.target].task);
                });
            });
            // Updates operations with no suggestion defined in input. See the case for algorithms
            topological.order.forEach(function(k){
                var task = topological.info[k].task;
                if (task.uiPorts.inputs.length === 0 && task.uiPorts.refs.length > 0){
                    task.uiPorts.refs.forEach(function(ref) {
                        Array.prototype.push.apply(task.uiPorts.inputs,
                            ref.uiPorts.inputs);
                    });
                }
            });
            uiCallback(result);
        }

        /* Retrieve data sources information */
        //https://jsfiddle.net/rcknr/fv289szj/
        var Chain = (function() {

            function bind(f, g) {
                return function(a, callback, errback) {
                    f(a, function(result) { return g(result, callback, errback); }, errback);
                };
            }

            function chain(args) {
                var f = args.shift();
                while (args.length > 0) {
                    f = bind(f, args.shift());
                }
                return f;
            }

            return {
                chain: chain
            };
        }());
        var args = [];
        dataSources.forEach(function(ds, i) {
            var fillInfoCallback = function(result) { loadFromDataSource(ds, result) };
            if (ds.forms.data_source && ds.forms.data_source.value){
                args.push(function(id, callback){
                    dataSourceLoader(ds.forms.data_source.value, callback)
                });
                args.push(function(result, callback){
                    loadFromDataSource(ds, result, callback);
                });
            }
        });
        if (args.length){
            Chain.chain(args)("goodbye", function(message) {
                lastStep()
            });
        } else {
            lastStep();
        }
    }
    return suggester;
}());
