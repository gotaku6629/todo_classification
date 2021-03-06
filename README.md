# todo_classification
やること自動分類Webアプリケーション
<p align="center">
<img src='imgs/todo_list.png' width="1000px"/>

## ネットワーク全体
<p align="center">
<img src='imgs/architecture.png' width="1000px"/>
   
   
## GitHubの使用方法まとめ
### 1.リポジトリをローカルにcloneする
   - 自分のPCのAtCoder用のディレクトリに移動して git clone [リポジトリのurl]　を実行

### 2.ブランチを作る
何か変更を行う時は, 必ずブランチを作る.
mainブランチに直接変更を加えることは, 他の開発者との変更衝突が起きるリスクが非常に高い.
mainへのpushは原則厳禁.
   - ローカルにブランチを作成する git branch [ブランチ名] を実行
   - 作成したブランチに移動する git checkout [ブランチ名] を実行
   - リモートにブランチを登録する git push -u origin [ブランチ名]を実行

### 3.変更を行う
作成したブランチ内で変更を行う.
必ず, 自分のいるブランチをチェックしてから変更を行う.
   - コードの変更を行う
   - 新規作成ファイルが存在する際, そのファイルをGit管理に登録する git add [ファイル名] を実行
   - コミットする git commit -a -m コミットメッセージ を実行
   - プッシュしてリモートに反映する git push origin を実行
   - コードの変更を行うに戻って, 変更が全て終わるまで繰り返す


### 4.マージ作業
3でpushした内容をGitHub上のmainへ反映させる


### 5.ブランチの削除
   - ローカルでmainブランチに移動する git checkout main を実行
   - ローカルに変更を反映する git pull origin main を実行
   - ローカルブランチを削除する git branch --delete [ブランチ名] を実行
