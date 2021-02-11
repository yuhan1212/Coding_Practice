'''
You are given a data structure of employee information,
which includes the employee's unique id, their importance value
and their direct subordinates' id.

For example, employee 1 is the leader of employee 2,
and employee 2 is the leader of employee 3. They have importance value 15,
10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]],
and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []].
Note that although employee 3 is also a subordinate of employee 1,
the relationship is not direct.

Now given the employee information of a company,
and an employee id, you need to return the total importance value of this employee
and all their subordinates.
'''



# Recursion
class Solution(object):
    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}
        # emap = {1:1, 5:2, 9:3}

        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
            # 1.importance + sum(dfs(2), dfs(9))
            # 5 + sum(5.importance + sum(dfs(None)) + 9.importance + sum(dfs(None)))
            # 5 + sum(3 + None + 3 + None)
            # 11
        return dfs(query_id)

# Iteration
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        # create a map to link employees' id and there position in list
        employee_in_list = {}
        for i in range(len(employees)):
            employee_in_list[employees[i].id] = i
        # employee_in_list = {1:1, 5:2, 9:3} 

        # initiate total_importance to the importance of the given id
        total_importance = employees[employee_in_list[id]].importance
        # 1.importance = 5

        # check and add if there is subordinates importance according to the givan id
        subordinates_list = employees[employee_in_list[id]].subordinates
        # subordinates_list = [2, 9]

        while subordinates_list != []:
            for i in subordinates_list:
                total_importance += employees[employee_in_list[subordinates_list.pop(0)]].importance
                subordinates_list += employees[employee_in_list[i]].subordinates
        return total_importance