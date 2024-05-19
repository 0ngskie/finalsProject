const express = require ('express')
const router = express.Router()

const employeeController = require('../controllers/employeeController')

// Create

router.post('/create', employeeController.createEmployee)

// Read

router.get('/', employeeController.getEmployees)
router.get('/manager', employeeController.getManagers)

// Update

router.put('/update/:id', employeeController.updateEmployee)

// Delete

router.delete('/delete/:id', employeeController.deleteEmployee)

module.exports = router;