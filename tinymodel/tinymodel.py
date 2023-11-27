import httpx
import os
import json 

from typing import Union, Literal

class TinyModelError(Exception):
    pass

class TinyModel:
    class Completions:
        def __init__(self, api_key, base_url):
            self.api_key = api_key
            self.base_url = base_url
            
        def request_completion(self, base_url, api_key, model, prompt, max_tokens, temperature):
            # Prepare the request payload
            payload = {
                "api_key": api_key,
                "model": model,
                "prompt": prompt,
                "max_tokens": max_tokens,
                "temperature": temperature
            }

            # Send the request
            endpoint = f"{base_url}/completion"

            try:
                #response = httpx.post(endpoint, json=payload)
                
                response = {
                    "id": "123123123",
                    "content": f"Dummy response from endpoint {endpoint} for model {model} with prompt {prompt}",
                    "created": 1701040299,
                    "model": model,
                    "system_fingerprint": "", 
                    "status": "success",
                    "system_message": "",
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                    "total_tokens": 0
                }
                
            except Exception as ex: 
                response = {"status":"error", "system_message": str(ex)}
              
            return response

        def create(self, model, prompt, max_tokens=512, temperature=0.8):
            
            if model not in ["philosophy", "literature"]:
                raise TinyModelError("Model must be 'philosophy' or 'literature'")
            
            # Enforce max_tokens limit
            if max_tokens > 512:
                raise TinyModelError("max_tokens cannot exceed 512")
            if max_tokens <= 0:
                max_tokens = 512

            # Logic to handle the completion request
            # For example, making an HTTP request to the API
            response = self.request_completion(self.base_url, self.api_key, model, prompt, max_tokens, temperature)
            
            return response

    def __init__(self, api_key):
        if api_key is None:
            api_key = os.environ.get("TINYMODEL_API_KEY")
        if api_key is None:
            raise TinyModelError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TINYMODEL_API_KEY environment variable"
            )
        
        self.api_key = api_key
        self.base_url = "https://etrack.ws/scriptai.svc/v1"
        
        self.completions = TinyModel.Completions(self.api_key, self.base_url)
        