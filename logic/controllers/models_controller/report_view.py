class Report_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Report controller"""
        print("connection to Report succeeded")
        self.cursor = cursor
        self.oracle = oracle

    def get_title_summary(self):
        total_annual_salary = self.cursor.execute('Select Annual_Total_Salary from dual').fetchone()[0]
        total_unit_sales = self.cursor.execute('Select Total_Unit_Sales from dual').fetchone()[0]
        total_material_order = self.cursor.execute('Select Total_Material_Order from dual').fetchone()[0]
        total_sales = self.cursor.execute('Select Total_Sales from dual').fetchone()[0]
        total_employees = self.cursor.execute('Select Total_Employees from dual').fetchone()[0]
        title_dict = {"total_annual_salary": total_annual_salary,
                      "total_unit_sales": total_unit_sales,
                      "total_material_order": total_material_order,
                      "total_sales": total_sales,
                      "total_employees": total_employees}
        return title_dict


    def AnnualDeptSal(self):
        """This Method will grab all the data from the Annual Dept View"""
        data = []
        self.cursor.execute(
            f"select dept_id , dept_name , annual_salary from vAnnualDeptSal")
        print(self.cursor)
        for dept_id, dept_name, annual_salary in self.cursor:
            data.append({"dept_id": dept_id,
                         "dept_name": dept_name,
                         "annual_salary": annual_salary})
        # print(data)
        print(len(data))
        return data

    def AverageSales(self):
        """This Method will grab all the data from the Average Sales View"""
        data = []
        self.cursor.execute(
            f"select customer_id , customer_name , sum_buying from vSalesAvg")
        print(self.cursor)
        for customer_id, customer_name, sum_buying in self.cursor:
            data.append({"customer_id": customer_id,
                         "customer_name": customer_name,
                         "sum_buying": sum_buying})
        # print(data)
        print(len(data))
        return data

    def OrderAvg(self):
        """This Method will grab all the data from the Order Average View"""
        data = []
        self.cursor.execute(
            f"select vendor_id, vendor_name, material_name, average_order from vOrderAvg")
        print(self.cursor)
        for vendor_id, vendor_name, material_name, average_order in self.cursor:
            data.append({"vendor_id": vendor_id,
                         "vendor_name": vendor_name,
                         "material_name": material_name,
                         "average_order": average_order})
        # print(data)
        print(len(data))
        return data

    def ProductSales(self):
        """This Method will grab all the data from the Product Sales View"""
        data = []
        self.cursor.execute(
            f"select product_name, total_unit_sales from vProductSales")
        print(self.cursor)
        for product_name, total_unit_sales in self.cursor:
            data.append({"product_name": product_name,
                         "Total_Unit_Sales": total_unit_sales
                         })
        # print(data)
        print(len(data))
        return data

    def ViewManager(self):
        """This Method will grab all the data from the View Employee View"""
        data = []
        self.cursor.execute(
            f"select dept_name, employee_per_department from vEmployees")
        print(self.cursor)
        for dept_name, employee_per_department in self.cursor:
            data.append({"dept_name": dept_name,
                         "emp_dept": employee_per_department})
        # print(data)
        print(len(data))
        return data
