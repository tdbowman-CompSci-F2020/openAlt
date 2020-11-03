def crossrefIngest(uniqueEvent, cursor, connection):

    t_license = None
    t_obj_id = None
    t_source_token = None
    t_occurred_at = None
    t_subj_id = None
    t_id = None
    t_terms = None
    t_message_action = None
    t_source_id = None
    t_timestamp = None
    t_relation_type_id = None

    for key, value in uniqueEvent.items():
        if key == "license":
            t_license = value
        elif key == "obj_id":
            t_obj_id = value
        elif (key == "source_token"):
            t_source_token = value
        elif (key == "occurred_at"):
            t_occurred_at = value
        elif (key == "subj_id"):
            t_subj_id = value
        elif (key == "id"):
            t_id = value
        elif (key == "terms"):
            t_terms = value
        elif (key == "message_action"):
            t_message_action = value
        elif (key == "source_id"):
            t_source_id = value
        elif (key == "timestamp"):
            t_timestamp = value
        elif (key == "relation_type_id"):
            t_relation_type_id = value

    # SQL which inserts into event table
    add_event = ("INSERT IGNORE INTO crossrefevent " "(license, objectID, sourceToken, occurredAt, subjectID, eventID, crossrefTermsOfUse, messageAction, sourceID, timeObserved, relationType) " "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    # Values to insert into event table
    data_event = (t_license, t_obj_id, t_source_token, t_occurred_at, t_subj_id,
                  t_id, t_terms, t_message_action, t_source_id, t_timestamp, t_relation_type_id)

    # add information to dataciteevent table
    cursor.execute(add_event, data_event)
    connection.commit()