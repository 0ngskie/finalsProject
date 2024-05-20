const repairJob = require('../model/repairjobs')
const mysqlCon = require('../model/mysqlCon')

// Create

module.exports.createRepairJob = (req, res) => {
    const{vehicle_id, employee_id, shop_id, problemType, description, startDate, endDate, status} = req.body;

    const query =`Insert into repairjob( vehicle_id, employee_id, shop_id, problemType, description, startDate, endDate, status) values (?, ?, ?, ?, ?, ?, ?, ?)`;
    
    const values = [vehicle_id, employee_id, shop_id, problemType, description, startDate, endDate, status];
    
    mysqlCon.query(query, values, (error, result) => {
        if (error) {
            console.error('Error creating repairjob:', error);
            return res.status(500).json({ error: 'Error creating repairjob' });
        }
        res.status(201).json({ "New repairjob": {...req.body, id: result.insertId } });
    })
}

// Read

module.exports.getRepairJobs = (req, res) => {
    const{ vehicle_id, employee_id, shop_id, problemType, description, startDate, endDate,status } = req.body;

    const query = 'Select * from repairjob' ;
    const values = [vehicle_id, employee_id, shop_id, problemType, description, startDate, endDate, status];

    mysqlCon.query(query, values, (error, result) => {
        if (error) {
            console.error('Error getting repairjobs:', error);
            return res.status(500).json({ error: 'Error getting repairjobs' });
        }
        res.status(200).json(result);
    })
}

// Update

module.exports.updateRepairJob = (req, res) => {
    const{ vehicle_id, employee_id, shop_id, problemType, description, startDate, endDate,status } = req.body;

    const query = `UPDATE repairjob SET vehicle_id = ?, employee_id = ?, shop_id = ?, problem_type =?, description = ?, startDate = ?, endDate = ?, status = ? WHERE id = ?`;
    const values = [vehicle_id, employee_id, shop_id, problemType, description, startDate, endDate, status];

    mysqlCon.query(query, values, (err, result) => {
        if (err) {
            console.error('Error updating repairjob:',err);
            return result.status(500).json({err: 'Error updating repairjob'});
        }
        res.status(200).json(result);
    })
}

// Delete
module.exports.deleteRepairJob = (req, res) => {
    const{ vehicle_id, employee_id, shop_id, problemType, description, startDate, endDate,status } = req.body;
    const query = `DELETE FROM repairjob WHERE id = ?`;
    const values = [vehicle_id, employee_id, shop_id, problemType, description, startDate, endDate, status];
    
    mysqlCon.query (query, values, (err, result) => {
        if(err){
            console.error('Error deleting reparjob:', err);
            return result.status(500).json({err: 'Error deleting reparjob'});
        }
    })
}
