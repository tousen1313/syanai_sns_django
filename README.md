# syanai_sns_django

|  URL | 機能 | 備考 |
| ---- | ------- | ---- |
| admin | db管理画面 | django既存機能 |
| signup | サインアップ画面 | |
| list | サインアップ画面 | |
| create | sns内容新規作成画面 | |
| detail/<int:pk> | sns詳細画面 | |
| login | ログイン処理を行う | |
| logout | ログアウト処理を行う | |
| good/<int:pk>/ | いいねを行う | |
| read/<int:pk> | 既読を行う | |

## model
### BoardModel
|  fieldname | type | 備考 |
| ---- | ------- | ---- |
| title | charField(maxlength=100) | snsのタイトル |
| content | TextField | snsの内容 |
| author | charField(maxlength=100) | snsのを記載したユーザー |
| snsimage | ImageField | snsの画像 |
| good | IntegerField | snsのいいね |
| read | IntegerField | snsの既読 |
| readtext | TextField | 既読したユーザーリスト |

## login 画面
![image](https://user-images.githubusercontent.com/77877016/226157824-9a22701d-1a6b-4c18-972e-ab3df3670a47.png)

## list 画面
<img width="981" alt="image" src="https://user-images.githubusercontent.com/77877016/226158584-5835b787-a895-4b86-8491-53800947e176.png">

## detail 画面
<img width="971" alt="image" src="https://user-images.githubusercontent.com/77877016/226158619-23969d37-392c-4e60-abbb-34a90306b535.png">
