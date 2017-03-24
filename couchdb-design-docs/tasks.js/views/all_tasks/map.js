function(doc) {
    if(doc.type == 'task'){
        emit(doc._id, {'description':doc.description, 'priority': doc.priority});
    }
}