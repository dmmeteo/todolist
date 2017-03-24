function(doc) {
    if(doc.type == 'task' && doc.status == 'completed'){
        emit(doc.status, {'description':doc.description, 'priority': doc.priority});
    }
}