
        if not account_number:
            return []
        
        url = 'http://www.bcove.com/services/viewer/htmlFederated?id=%s&videoId=%s&videoType=3&videoId=%s' % (account_number, video_id, video_id)
        data = self._download_xml(url, video_id)
        data = xmltodict.parse(data)
        
        if data.get('error'):
            raise ExtractorError(data['error'], expected=True)
        
        if data.get('status')!= 'ok':
            raise