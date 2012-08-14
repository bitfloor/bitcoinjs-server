var logger = require('./logger');

try {
  module.exports = require('bindings')('native.node');
} catch (err) {
  logger.error(err.message);
  process.exit(1);
}
