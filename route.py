import subprocess
import urllib
import urllib.parse

from flask import Response, stream_with_context

from .setup import *


#########################################################
# Plex Proxy
#########################################################
@P.blueprint.route('/proxy/<sub>', methods=['GET', 'POST'])
def proxy(sub):
    # 설정 저장
    logger.info(f"HDHomerun Proxy Sub: {sub}")
    if sub == 'discover.json':
        try:
            ddns = F.SystemModelSetting.get('ddns')
            data = {"FriendlyName":"HDHomeRun CONNECT","ModelNumber":"HDHR4-2US","FirmwareName":"hdhomerun4_atsc","FirmwareVersion":"20190621","DeviceID":"104E8010","DeviceAuth":"UF4CFfWQh05c3jROcArmAZaf","BaseURL":"%s/hdhomerun/proxy" % ddns,"LineupURL":"%s/hdhomerun/proxy/lineup.json" % ddns,"TunerCount":20}
            return jsonify(data)
        except Exception as e: 
            logger.error('Exception:%s', e)
            logger.error(traceback.format_exc())
    elif sub == 'lineup_status.json':
        try:
            data = {"ScanInProgress":0,"ScanPossible":1,"Source":"Cable","SourceList":["Antenna","Cable"]}
            return jsonify(data)
        except Exception as e: 
            logger.error('Exception:%s', e)
            logger.error(traceback.format_exc())
    elif sub == 'lineup.json':
        try:
            lineup = []
            channel_list = ModelHDHomerunChannel.channel_list(only_use=True)
            ddns = F.SystemModelSetting.get('ddns')
            for c in channel_list:
                lineup.append({'GuideNumber': str(c.ch_number), 'GuideName': c.scan_name, 'URL': c.url})
            return jsonify(lineup)
        except Exception as e: 
            logger.error('Exception:%s', e)
            logger.error(traceback.format_exc())


@P.blueprint.route('/video', methods=['POST'])
def video():
    arg = {}
    arg['play_title'] = request.form['play_title']
    arg['play_source_src'] = request.form['play_source_src']
    arg['play_source_type'] = request.form['play_source_type']
    return render_template(f'{P.package_name}_video.html', arg=arg)
    

  

foo = None