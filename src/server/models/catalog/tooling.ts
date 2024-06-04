import mongoose from "mongoose";

const toolingSchema = new mongoose.Schema({
    _id: {
        Number,
        required: true
    },  
    Multipler: String,
    Catergory: String,
    "Mutliplier Value": Number,
    Comments: String
});