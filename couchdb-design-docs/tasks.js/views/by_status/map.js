function(doc) {
    if(doc.type == 'task'){
        emit(doc.status, null);
    }
}