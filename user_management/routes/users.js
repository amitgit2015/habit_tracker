const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const authenticateToken = require('../middleware/auth'); // If you have JWT middleware

// Create user
router.post('/', userController.createUser);

// Get user by ID
router.get('/:id', authenticateToken, userController.getUser);

// Update user
router.put('/:id', authenticateToken, userController.updateUser);

// Delete user
router.delete('/:id', authenticateToken, userController.deleteUser);

module.exports = router;
