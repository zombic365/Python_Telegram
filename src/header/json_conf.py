import json
from easydict import EasyDict

class JsonManager:
    def __init__(self, file_path):
        self.values = EasyDict()
        if file_path:
            self.file_path = file_path #### json 파일 경로 저장
            self.reload()

    def clear(self):
        self.values.clear() #### 파이썬에서 불러드린 json dict 초기화

    def reload(self):
        self.clear()
        if self.file_path:
            with open(self.file_path, 'r') as f:
                self.values.update(json.load(f)) #### json 데이터 불러오기

    def update(self, in_dict):
        """기존 설정에 새로운 설정을 업데이트한다(최대 3레벨까지만)""" #### 이 부분 아직 이해 못함
        for (k1, v1) in in_dict.items():
            if isinstance(v1, dict):
                for (k2, v2) in v1.items():
                    if isinstance(v2, dict):
                        for (k3, v3) in v2.items():
                            self.values[k1][k2][k3] = v3
                    else:
                        self.values[k1][k2] = v2
            else:
                self.values[k1] = v1
        with open(self.file_path, 'w') as f:
            json.dump(dict(self.values), f, indent='\t') #### json 업데이트된 값을 다시 파일에 저장
