function(doc) {
    if(doc.type == 'task' && doc.status == 'active'){
        emit(doc.status, doc);
    }
}