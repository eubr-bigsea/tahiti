/******************************************************************************
* Attribute suggestion for Citron from Tahiti (both Lemonade Project modules).
* (c) 2017 Speed Labs - Departamento de Ciência da Computação - UFMG (Brazil).
*****************************************************************************/
var TahitiAttributeSuggester = (function () {
    var suggester = {};

    /* Private functions */
    var flatArrayOfArrays = function flatArrayOfArrays(listOfAttrs){
        return Array.prototype.concat.apply([], listOfAttrs.map(
                        function(item) {return item.attributes;}));
    };
    var cloneDeep = function(o){
      let newO
      let i

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
          topological.info[flow.source_id].targets.push(
          {
              target: flow.target_id,
              targetPortId: flow.target_port
          });
      });
      // 2. topological sort
      Object.keys(topological.info).forEach(function visit(taskId, ancestors) {
          var task = topological.info[taskId];

          // if already exists, do nothing
          if (visited[taskId]) return;

          if (!Array.isArray(ancestors)) ancestors = [];

          ancestors.push(taskId);

          visited[taskId] = true;

          task.targets.forEach(function (after) {
              if (ancestors.indexOf(after) >= 0)  // if already in ancestors, a closed chain exists.
                  throw new Error('closed chain : ' + after.target + ' is in ' + taskId);
              visit(after.target.toString(), ancestors.map(function (v) { return v })); // recursive call
          });
          sorted.unshift(taskId);
      });
      return {order: sorted, info: topological.info};
    };
    var loadFromDataSource = function(task, result, callback) {
        Array.prototype.push.apply(task.uiPorts.output, result);
        if (callback) {
            callback(result);
        }
    }
    var onlyField = function(task, field, many) {
        if (many === undefined || !many ) {
            Array.prototype.push.apply(task.uiPorts.output,
                task.forms[field].value.split(', ').map(function(attr){return attr.trim() }));
        } else if (task.forms[field]) {
            Array.prototype.push.apply(task.uiPorts.output, task.forms[field].value);
        }
        task.uiPorts.output.sort();
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
         task.uiPorts.output.sort();
    }
    var copyAllInputsRemoveDuplicated = function(task) {
        var attrs = flatArrayOfArrays(task.uiPorts.inputs).sort();
        task.uiPorts.output = attrs.filter(
            function(item, index, inputArray ) {
                return inputArray.indexOf(item) === index;
             }
        );
    };
    var copyInput = function(task) {
        task.uiPorts.output = flatArrayOfArrays(task.uiPorts.inputs).sort();
    };
    var joinSuffixDuplicatedAttributes = function(task) {
        /* Group attributes by name */
        let groupedFields = flatArrayOfArrays(task.uiPorts.inputs).reduce(function(acc, val){
            (acc[val] = acc[val] || []).push(val);
            return acc;
        }, {});
        /* Change the name of duplicated attributes, suffixing a number */
        let result = [];
        for(var property in groupedFields) {
            if (groupedFields.hasOwnProperty(property)) {
                if (groupedFields[property].length > 1){
                    for(var i = 0; i < groupedFields[property].length - 1; i++){
                        result.push(property + '_' + i);
                    }
                } else {
                    result.push(property);
                }
            }
        }
        //task.uiPorts.output = flatArrayOfArrays(task.uiPorts.inputs);
        task.uiPorts.output = result.sort();
    }
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
        } else {
            console.error('Alias ' + alias + ' does not exist for task ' +
                task.id + '(' + task.operation.slug + ')');
        }
        Array.prototype.push.apply(task.uiPorts.output, aliases);
        task.uiPorts.output.sort();
    }

    var copyFromOnlyOneInput = function(task, id) {
        let inputs = task.uiPorts.inputs.filter(
            function(input) {
                return parseInt(input.targetPortId) === parseInt(id);
            }) || [];
        task.uiPorts.output = flatArrayOfArrays(inputs).sort();
    }
    /* Public methods */
    suggester.compute = function(workflow, dataSourceLoader, uiCallback) {

        var dataSources = [];
        workflow.tasks.forEach(function(task){
            task.uiPorts = {inputs: [], output: []}
            var isDataSource = [18, 53].indexOf(parseInt(task.operation.id)) > -1;
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

            var result = {};
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
                    topological.info[follow.target].task.uiPorts.inputs.push(
                        {targetPortId: follow.targetPortId,
                            attributes: task.uiPorts.output});
                });
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