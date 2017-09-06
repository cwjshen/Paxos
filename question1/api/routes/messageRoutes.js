'use strict';
module.exports = function(app) {
  var messages = require('../controllers/messageController');

  // MessageHash Routes
  app.route('/messages')
    .get(messages.list_all_messages)
    .post(messages.create_a_message);


  app.route('/messages/:hash')
    .get(messages.get_original_message);
};

