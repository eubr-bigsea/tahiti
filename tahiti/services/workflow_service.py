import json
import typing
import uuid
from tahiti.models import *

class WorkflowService(object):
    def get_tasks_for_modeling(self, workflow: Workflow, 
            task_type: str, method: str) -> typing.List[Task]:

        common = self._get_common_tasks(workflow)

        if task_type == 'clustering':
            return common + self._get_tasks_for_clustering(workflow, method)
        elif task_type == 'regression':
            return common + self._get_tasks_for_regression(workflow, method)

        return common


    def _get_common_tasks(self, workflow: Workflow) -> typing.List[Task]:
        result = []
        split = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='split', Platform.id==1000).first()

        forms = json.dumps(
            {"strategy": {"value": "split"}, "ratio": {"value": "0.8"}}
        )
        result.append(Task(
            id=str(uuid.uuid4()),
            operation=split, name=split.name, 
            workflow=workflow, forms=forms, left=0, top=0,
            display_order=0, z_index=0))
        
        sample = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='sample', Platform.id==1000).first()

        forms = json.dumps(
            {"type": {"value": "value"}, "value": {"value": "10000"}}
        )
        result.append(Task(
            id=str(uuid.uuid4()),
            operation=sample, name=sample.name, 
            workflow=workflow, forms=forms, left=0, top=0,
            display_order=0, z_index=0))
        return result


    def _get_tasks_for_clustering(self, workflow: Workflow, 
            method: str) -> typing.List[Task]:

        k_means = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='k-means', Platform.id==1000).first()
        result = []
        if k_means and method == 'fast':
            k = {"list": ["2", "4", "8", "16"], "type": "list"}
            alg_type = ["kmeans"]
            dist = ["euclidean"]
            init_mode = ["k-means||"]
            forms = json.dumps({
                "number_of_clusters": {
                    "value": k, "internalValue": k, "enabled": True}, 
                "type": {"value": alg_type, "internalValue": alg_type}, 
                "init_mode": {"value": init_mode, "internalValue": init_mode},
                "distance": {"value": dist, "internalValue": dist}
            })
            result.append(Task(
                id=str(uuid.uuid4()),
                operation=k_means, name=k_means.name, 
                workflow=workflow, forms=forms, left=0, top=0,
                display_order=2, z_index=2))

        return result

    def _get_tasks_for_regression(self, workflow: Workflow, 
            method: str) -> typing.List[Task]:

        result = []

        evaluator = Operation.query.join(Operation.platforms).filter(
            Operation.slug=='evaluator', Platform.id==1000).first()
        forms = json.dumps(
            {"task_type": {"value": "regression"}, "reg_metric": {"value": "rmse"}}
        )
        result.append(Task(
            id=str(uuid.uuid4()),
            operation=evaluator, name=evaluator.name, 
            workflow=workflow, forms=forms, left=0, top=0,
            display_order=0, z_index=0))

        features = Operation.query.join(Operation.platforms).filter(
            Operation.slug=='features', Platform.id==1000).first()

        workflow_form = json.loads(workflow.forms)

        forms = json.dumps(
                {"features": {"value": [
                    {"name": workflow_form.get('$meta').get('value').get('label'), 
                        "usage": "label", "enable": True, 
                        "feature_type": "numerical", "transform": "keep"}]}}
        )
        result.append(Task(
            id=str(uuid.uuid4()),
            operation=features, name=features.name, 
            workflow=workflow, forms=forms, left=0, top=0,
            display_order=0, z_index=0))


        if method == 'fast':
            random_forest = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='random-forest-regressor', Platform.id==1000).first()

            trees = {"list": ["100"], "type": "list"}
            depth = {"list": ["2", "6"], "type": "list"}
            forms = json.dumps({
                "num_trees": {
                    "value": trees, "internalValue": trees}, 
                "max_depth": {"value": depth, "internalValue": depth},
            })
            result.append(Task(
                id=str(uuid.uuid4()),
                operation=random_forest, name=random_forest.name, 
                workflow=workflow, forms=forms, left=0, top=0,
                display_order=2, z_index=2))

        elif method == 'interpretable':
            dt = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='decision-tree-regressor', Platform.id==1000).first()

            depth = {"list": ["6"], "type": "list"}
            forms = json.dumps({
                "max_depth": {"value": depth, "internalValue": depth},
            })
            result.append(Task(
                id=str(uuid.uuid4()),
                operation=dt, name=dt.name, 
                workflow=workflow, forms=forms, left=0, top=0,
                display_order=3, z_index=3))
        elif method == 'performance':
            grid = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='grid', Platform.id==1000).first()

            forms = json.dumps({"strategy": {"value": "random"}, 
                "max_iterations": {"value": 30}})
            result.append(Task(
                id=str(uuid.uuid4()),
                operation=grid, name=grid.name, 
                workflow=workflow, forms=forms, left=0, top=0,
                display_order=0, z_index=0))

            random_forest = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='random-forest-regressor', Platform.id==1000).first()

            trees = {"type": "range", "min": 80, "max": 200, "distribution": "uniform"}
            depth = {"type": "range", "min": 5, "max": 10, "distribution": "uniform"}
            feat_subset = ["auto"]
            forms = json.dumps({
                "num_trees": {
                    "value": trees, "internalValue": trees}, 
                "max_depth": {"value": depth, "internalValue": depth},
                "feature_subset_strategy": {"value": feat_subset, 
                    "internalValue": feat_subset}, 
            })
            result.append(Task(
                id=str(uuid.uuid4()),
                operation=random_forest, name=random_forest.name, 
                workflow=workflow, forms=forms, left=0, top=0,
                display_order=2, z_index=2))

            gbt = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='gbt-regressor', Platform.id==1000).first()
            depth = {"type": "range", "min": 5, "max": 10, "distribution": "uniform"}
            forms = json.dumps({
                "max_depth": {"value": depth, "internalValue": depth},
            })
            result.append(Task(
                id=str(uuid.uuid4()),
                operation=gbt, name=gbt.name, 
                workflow=workflow, forms=forms, left=0, top=0,
                display_order=2, z_index=2))



        if method in ('fast', 'interpretable'):
            linear_reg = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='linear-regression', Platform.id==1000).first()

            elastic_net = {"list": ["0.1", "1.0", "3.0"], "type": "list"}
            forms = json.dumps({
                "elastic_net": {"value": elastic_net, "internalValue": elastic_net},
            })
            result.append(Task(
                id=str(uuid.uuid4()),
                operation=linear_reg, name=linear_reg.name, 
                workflow=workflow, forms=forms, left=0, top=0,
                display_order=3, z_index=3))

            grid = Operation.query.join(Operation.platforms).filter(
                Operation.slug=='grid', Platform.id==1000).first()

            forms = json.dumps({"strategy": {"value": "grid"}})
            result.append(Task(
                id=str(uuid.uuid4()),
                operation=grid, name=grid.name, 
                workflow=workflow, forms=forms, left=0, top=0,
                display_order=0, z_index=0))



        return result



