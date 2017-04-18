from . import * 
from app.irsystem.models.matrix import Matrix
from app.irsystem.models.redisconn import RedisConn as RedisConn 
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder
from app.irsystem.models.search import query_info
from app.irsystem.models.search import process_query


project_name = "Movie Character Similarity"
net_id = "Chris Bora: cdb239, Jacob Cooper: jtc267, Kurt Shuster: kls294, Jordan Stout: jds459"

@irsystem.route('/', methods=['GET'])
def search():
        query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
                data = process_query(query)
                info = query_info(query)
                return render_template('results.html', data=data, query=info)
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)


