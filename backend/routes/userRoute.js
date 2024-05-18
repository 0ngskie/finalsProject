const express = require ('express')
const router = express.Router()

const userController = require('../controllers/userController')

// Create

router.post('/create', userController.createUser)

// Read

router.get('/user', userController.getUsers)

// Update

router.put('/update/:id', userController.updateUser)

// Delete

router.delete('/delete/:id', userController.deleteUser)

module.exports = router;