// db/pool.js

const { Pool } = require('pg');
module.exports = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'user_management',
  password: '',
  port: 5432
});