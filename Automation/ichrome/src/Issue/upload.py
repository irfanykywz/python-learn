root_id = (await
           tab.send('DOM.getDocument'))['result']['root']['nodeId']
nodeId = (await
          tab.send('DOM.querySelector',
                   nodeId=root_id,
                   selector='input[type="file"]'))['result']['nodeId']
await tab.send('DOM.setFileInputFiles',
               files=[str(path.absolute())],
               nodeId=nodeId)