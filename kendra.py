import boto3


class Kendra:

    kendra = boto3.client('kendra', region_name='us-east-1')
    index_id = '<enter your kendra index id here>'

    def query(self, query):
        response = self.kendra.query(QueryText=query, IndexId=self.index_id)
        for query_result in response['ResultItems']:
            begin = 0
            end = 0
            if query_result['Type'] == 'ANSWER':
                answer = query_result['AdditionalAttributes'][0]['Value']['TextWithHighlightsValue']
                highlight = answer['Highlights']
                for obj in highlight:
                    if obj['TopAnswer'] is True:
                        begin = obj['BeginOffset']
                        end = obj['EndOffset']
                if end == 0:
                    answer_text = answer['Text']
                else:
                    answer_text = answer['Text'][begin:end]
                return answer_text

