'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var MessageSchema = new Schema({
  message: {
    type: String,
    required: 'Error: Please enter a message to hash',
    unique: true
  },
  digest: {
    type: String,

  }
});

module.exports = mongoose.model('Messages', MessageSchema);

