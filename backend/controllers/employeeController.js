const Employee = require("../model/employees")
const mysqlCon = require('../mysql/mysqlCon')

// Create

module.exports.createEmployee = (req, res) => {
    const { employee_id, user_id, specialty, manager_id, shop_id } = req.body;

    const query = `INSERT INTO employee (employee_id, user_id, specialty, manager_id, shop_id) 
                   VALUES (?, ?, ?, ?, ?)`;

    const values = [employee_id, user_id, specialty, manager_id, shop_id];

    mysqlCon.query(query, values, (err, result) => {
        if (err) {
            console.error('Error creating an Employee',err);
            res.status(500).send(err);
        } else {
            res.status(201).json({"New Employee" : {...req.body, id: result.insertId}});
        }
    })
}

// Read

module.exports.getEmployees = (req, res) => {
    const query = `SELECT * FROM employee`;

    mysqlCon.query(query, (err, result) => {
        if (err) {
            console.error('Error fetching Employees',err);
            return res.status(500).json({err: 'Error fetching Employees'});
        } else {
            res.status(200).json(result);
        }
    })
}

// Update

module.exports.updateEmployee = (req, res) => {
    const { employee_id, user_id, specialty, manager_id, shop_id } = req.body;

    const query = `UPDATE employee SET employee_id =?, user_id =?, specialty =?, manager_id =?, shop_id =? WHERE employee_id =?`;
   
    const values = [employee_id, user_id, specialty, manager_id, shop_id, req.params.id];

    mysqlCon.query(query, values, (err, result) => {
        if (err) {
            console.error('Error updating Employee',err);
            return res.status(500).json({err: 'Error updating Employee'});
        } else {
            res.status(200).json(result);
        }
    })
}

// Delete

module.exports.deleteEmployee = (req, res) => {
    const query = `DELETE FROM employee WHERE employee_id =?`;

    const values = [req.params.id];

    mysqlCon.query(query, values, (err, result) => {
        if (err) {
            console.error('Error deleting Employee',err);
            return res.status(500).json({err: 'Error deleting Employee'});
        } else {
            res.status(200).json(result);
        }
    })
}