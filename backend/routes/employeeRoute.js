const express = require ('express')
const router = express.Router()

const employeeController = require('../controllers/employeeController')

// Create

router.post('/create', userController.createUser)

// Read

router.get('/', employeeController.getEmployees)
router.get('/manager', employeeController.getManagers)

// Update

router.put('/update/:id', userController.updateUser)

// Delete

router.delete('/delete/:id', userController.deleteUser)

module.exports = router;