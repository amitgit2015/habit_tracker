// ----------- controllers/userController.js
const bcrypt = require('bcrypt');
const pool = require('../db/pool');

exports.createUser = async (req, res) => {
  const { username, password, role } = req.body;
  try {
    const hashedPassword = await bcrypt.hash(password, 10);
    const result = await pool.query(
      'INSERT INTO users (username, password, role) VALUES ($1, $2, $3) RETURNING *',
      [username, hashedPassword, role]
    );
    res.status(201).json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
};

exports.getUser = async (req, res) => {
  const userId = req.params.id;
  try {
    const result = await pool.query('SELECT id, username, role FROM users WHERE id = $1', [userId]);
    if (!result.rows.length) return res.status(404).json({ message: 'User not found' });
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
};

exports.updateUser = async (req, res) => {
  const userId = req.params.id;
  const { username, password, role } = req.body;
  try {
    let query = 'UPDATE users SET username = $1, role = $2 WHERE id = $3 RETURNING *';
    let params = [username, role, userId];
    if (password) {
      const hashedPassword = await bcrypt.hash(password, 10);
      query = 'UPDATE users SET username = $1, password = $2, role = $3 WHERE id = $4 RETURNING *';
      params = [username, hashedPassword, role, userId];
    }
    const result = await pool.query(query, params);
    if (!result.rows.length) return res.status(404).json({ message: 'User not found' });
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
};

exports.deleteUser = async (req, res) => {
  const userId = req.params.id;
  try {
    const result = await pool.query('DELETE FROM users WHERE id = $1 RETURNING *', [userId]);
    if (!result.rows.length) return res.status(404).json({ message: 'User not found' });
    res.json({ message: 'User deleted' });
  } catch (err) {
    res.status(500).json({ message: 'Server error' });
  }
};
