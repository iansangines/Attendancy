import json
from django.utils.translation import ugettext_lazy as _
from django.db.models.query import QuerySet

def event_serializer(events):
    """
    serialize event model
    """
    css_class = {'0': '',
 	    '1': 'event-warning', 
            '2': 'event-info', 
            '3': 'event-success', 
            '4': 'event-inverse', 
            '5' : 'event-special', 
	    '6' : 'event-important'}
    objects_body = []
    if isinstance(events, QuerySet):
	cont = 0
	assig = 1
        for event in events:
		if cont != 0:
			if (event.title != prevtitle ):
				if assig == 6:
					assig = 0
				else:
					assig = assig + 1


		prevtitle = event.title
           	field = {"id": event.pk,
                	"title": event.title,
                	"url": event.url,
                	"class": css_class[str(assig)],
                	"start": event.start_timestamp,
                	"end": event.end_timestamp
            	}
            	objects_body.append(field)
		cont = cont + 1
    objects_head = {"success": 1}
    objects_head["result"] = objects_body
    return json.dumps(objects_head)
