'use strict';


var mongoose = require('mongoose');
var Message = mongoose.model('Messages');
var SHA256 = require("crypto-js/sha256");

exports.list_all_messages = function(req, res) {
  Message.find({}, function(err, message) {
    if (err)
      res.send(err);
    res.json(message);
  });
};

exports.get_original_message = function(req, res) {
  var hash = req.params.hash;
  Message.find({digest: hash}, function(err, message) {
  	if (message.length == 0)
  		res.sendStatus(404);  		
  	else
  		res.json({'message': message[0].message});
  });

};

exports.create_a_message = function(req, res) {
	var new_message = new Message();
	var message = req.body.message;
	var digest = SHA256(message);

	new_message.message = message;
	new_message.digest = digest;

	// Save to database
	new_message.save();

	res.json({"digest": new_message.digest});
};