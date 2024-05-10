import json


db_path="db/tasks.json"

class Store:
    def __init__(self):
        '''
        Function to read all info from db on initialization, including the id
        '''
        with open(db_path, "r") as file:
            self.data=json.load(file)
            self.id=self.data["id"]

    def add_task(self, task_str):
        '''
        function to add a task in local data
        ARGS: 
            task_str: the task string
        '''
        self.data["tasks"].append({"task":task_str, "task_id":self.id, "status":"pending"})
        self.id+=1
        self.data["id"]+=1

    def delete_task(self, task_id):
        '''
        function to delete a task given the task_id
        ARGS:
            task_id: ID of the task to be deleted
        '''
        for task in self.data["tasks"]:
            if task["task_id"]==task_id:
                self.data["tasks"].remove(task)

    def complete_task(self, task_id):
        '''
        function to mark a task completed given the task_id
        ARGS:
            task_id: ID of the task to be marked as complete
        '''
        for task in self.data["tasks"]:
            if task["task_id"]==task_id:
                task["status"]="complete"

    def get_pending(self):
        '''
        function to get all pending tasks
        RETURNS:
            List of {"task":task_str, "task_id":self.id, "status":"pending"}
        '''
        return [task for task in self.data["tasks"] if task["status"]=="pending"]

    def get_complete(self):
        '''
        function to get all complete tasks
        RETURNS:
            List of {"task":task_str, "task_id":self.id, "status":"complete"}
        '''
        return [task for task in self.data["tasks"] if task["status"]=="complete"]

    def get_all(self):
        '''
        function to get all tasks
        RETURNS:
            List of {"task":task_str, "task_id":self.id, "status":"complete"}
        '''
        return self.data["tasks"]

    def id_status(self, task_id):
        '''
        function to check if a task with the given id exists or not and if it is complete or pending
        ARGS:
            task_id: id to be searched
        RETURNS:
            "-1" if a task with the id doesn't exist
            status as a string if a task with the id exists
        '''
        for task in self.data["tasks"]:
            if task["task_id"]==task_id:
                return task["status"]
            else:
                return "-1"
    
    def write_state(self):
        with open(db_path, "w") as file:
            json.dump(self.data, file, indent=4)