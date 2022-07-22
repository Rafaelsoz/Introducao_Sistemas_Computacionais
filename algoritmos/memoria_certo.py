{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"memoria_certo.py","provenance":[],"collapsed_sections":[]},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["'''MAQUINA DE ESTADOS'''\n","import numpy as np\n","import pandas as pd"],"metadata":{"id":"dvF2Xe1ArWmN"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["memoria = pd.DataFrame(np.zeros((16,4)), columns = ['e1', 'e0', 'b', 'sp'])\n","\n","#Preencher a SP\n","for i in range(16):\n","  if i % 2 != 0:\n","    memoria['sp'].iloc[i] = 1\n","#Preencher o B\n","for i in range(2, 16, 4):\n","  memoria['b'].iloc[i] = 1\n","  memoria['b'].iloc[i + 1] = 1\n","#Preencher o e0\n","for i in range(4, 16, 8):\n","  memoria['e0'].iloc[i] = 1\n","  memoria['e0'].iloc[i + 1] = 1\n","  memoria['e0'].iloc[i + 2] = 1\n","  memoria['e0'].iloc[i + 3] = 1\n","#Preencher e1\n","for i in range(8, 16):\n","  memoria['e1'].iloc[i] = 1\n","memoria"],"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":551},"id":"WCkexApBNIM7","executionInfo":{"status":"ok","timestamp":1653571750466,"user_tz":180,"elapsed":276,"user":{"displayName":"Rafael Soz","userId":"07557259794887019026"}},"outputId":"7af70f9a-1d5a-4c87-b816-48858d2839fb"},"execution_count":null,"outputs":[{"output_type":"execute_result","data":{"text/plain":["     e1   e0    b   sp\n","0   0.0  0.0  0.0  0.0\n","1   0.0  0.0  0.0  1.0\n","2   0.0  0.0  1.0  0.0\n","3   0.0  0.0  1.0  1.0\n","4   0.0  1.0  0.0  0.0\n","5   0.0  1.0  0.0  1.0\n","6   0.0  1.0  1.0  0.0\n","7   0.0  1.0  1.0  1.0\n","8   1.0  0.0  0.0  0.0\n","9   1.0  0.0  0.0  1.0\n","10  1.0  0.0  1.0  0.0\n","11  1.0  0.0  1.0  1.0\n","12  1.0  1.0  0.0  0.0\n","13  1.0  1.0  0.0  1.0\n","14  1.0  1.0  1.0  0.0\n","15  1.0  1.0  1.0  1.0"],"text/html":["\n","  <div id=\"df-a572317b-ea7d-40ae-b946-1e6bb630fa1b\">\n","    <div class=\"colab-df-container\">\n","      <div>\n","<style scoped>\n","    .dataframe tbody tr th:only-of-type {\n","        vertical-align: middle;\n","    }\n","\n","    .dataframe tbody tr th {\n","        vertical-align: top;\n","    }\n","\n","    .dataframe thead th {\n","        text-align: right;\n","    }\n","</style>\n","<table border=\"1\" class=\"dataframe\">\n","  <thead>\n","    <tr style=\"text-align: right;\">\n","      <th></th>\n","      <th>e1</th>\n","      <th>e0</th>\n","      <th>b</th>\n","      <th>sp</th>\n","    </tr>\n","  </thead>\n","  <tbody>\n","    <tr>\n","      <th>0</th>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","    </tr>\n","    <tr>\n","      <th>1</th>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","    </tr>\n","    <tr>\n","      <th>2</th>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","    </tr>\n","    <tr>\n","      <th>3</th>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","    </tr>\n","    <tr>\n","      <th>4</th>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","    </tr>\n","    <tr>\n","      <th>5</th>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","    </tr>\n","    <tr>\n","      <th>6</th>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","    </tr>\n","    <tr>\n","      <th>7</th>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","    </tr>\n","    <tr>\n","      <th>8</th>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","    </tr>\n","    <tr>\n","      <th>9</th>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","    </tr>\n","    <tr>\n","      <th>10</th>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","    </tr>\n","    <tr>\n","      <th>11</th>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","    </tr>\n","    <tr>\n","      <th>12</th>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","      <td>0.0</td>\n","    </tr>\n","    <tr>\n","      <th>13</th>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","      <td>1.0</td>\n","    </tr>\n","    <tr>\n","      <th>14</th>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","      <td>0.0</td>\n","    </tr>\n","    <tr>\n","      <th>15</th>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","      <td>1.0</td>\n","    </tr>\n","  </tbody>\n","</table>\n","</div>\n","      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a572317b-ea7d-40ae-b946-1e6bb630fa1b')\"\n","              title=\"Convert this dataframe to an interactive table.\"\n","              style=\"display:none;\">\n","        \n","  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n","       width=\"24px\">\n","    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n","    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n","  </svg>\n","      </button>\n","      \n","  <style>\n","    .colab-df-container {\n","      display:flex;\n","      flex-wrap:wrap;\n","      gap: 12px;\n","    }\n","\n","    .colab-df-convert {\n","      background-color: #E8F0FE;\n","      border: none;\n","      border-radius: 50%;\n","      cursor: pointer;\n","      display: none;\n","      fill: #1967D2;\n","      height: 32px;\n","      padding: 0 0 0 0;\n","      width: 32px;\n","    }\n","\n","    .colab-df-convert:hover {\n","      background-color: #E2EBFA;\n","      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n","      fill: #174EA6;\n","    }\n","\n","    [theme=dark] .colab-df-convert {\n","      background-color: #3B4455;\n","      fill: #D2E3FC;\n","    }\n","\n","    [theme=dark] .colab-df-convert:hover {\n","      background-color: #434B5C;\n","      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n","      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n","      fill: #FFFFFF;\n","    }\n","  </style>\n","\n","      <script>\n","        const buttonEl =\n","          document.querySelector('#df-a572317b-ea7d-40ae-b946-1e6bb630fa1b button.colab-df-convert');\n","        buttonEl.style.display =\n","          google.colab.kernel.accessAllowed ? 'block' : 'none';\n","\n","        async function convertToInteractive(key) {\n","          const element = document.querySelector('#df-a572317b-ea7d-40ae-b946-1e6bb630fa1b');\n","          const dataTable =\n","            await google.colab.kernel.invokeFunction('convertToInteractive',\n","                                                     [key], {});\n","          if (!dataTable) return;\n","\n","          const docLinkHtml = 'Like what you see? Visit the ' +\n","            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n","            + ' to learn more about interactive tables.';\n","          element.innerHTML = '';\n","          dataTable['output_type'] = 'display_data';\n","          await google.colab.output.renderOutput(dataTable, element);\n","          const docLink = document.createElement('div');\n","          docLink.innerHTML = docLinkHtml;\n","          element.appendChild(docLink);\n","        }\n","      </script>\n","    </div>\n","  </div>\n","  "]},"metadata":{},"execution_count":4}]},{"cell_type":"code","source":["def controle(estado, botao, sensor_porta):\n","  '''LOGICA DE TRANSIÇÃO'''\n","  if estado == 0:\n","    if botao == 1:\n","      estado = 1\n","  elif estado == 1:\n","    if sensor_porta == 1:\n","      estado = 2\n","  elif estado == 2:\n","    if botao == 1:\n","      estado = 0\n","\n","  '''LOGICA DE AÇÃO'''\n","  if estado == 0:\n","    buzina = 0\n","    luz_vermelha = 0\n","  if estado == 1:\n","    buzina = 0\n","    luz_vermelha = 1\n","  if estado == 2:\n","    buzina = 1\n","    luz_vermelha = 1\n","  if estado == 3:\n","    buzina = 0\n","    luz_vermelha = 0\n","\n","  return estado, buzina, luz_vermelha"],"metadata":{"id":"KqcNVzzUdX20"},"execution_count":null,"outputs":[]}]}