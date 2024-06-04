import mongoose from "mongoose";

const processSchema = new mongoose.Schema({
    _id: {
        Number,
        required: true
    },  
    Process: String,
    Category: String,
    "Unit Cost": Number,
    "Unit": String,
    "Tooling Required": Boolean,
    "Near Net Shape": Boolean,
    "Process Multiplier": String,
    "Comments": String
});

const Process = mongoose.model('Process', processSchema);
module.exports = Process;
