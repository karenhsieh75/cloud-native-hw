# cloud-native-hw

本專案是為了完成 GitHub 操作練習作業，涵蓋了以下項目：

## 作業項目

- 建立 Public Repo
- 撰寫並修改 README.md
- 建立非 main 的 branch：`hw-p`, `hw-f`
- 建立並管理 Issue 與 Issue Template
- 建立 Pull Request 並留言
- 設定 GitHub Actions，自動化執行 CI 任務

## 分支說明

- `main`：主分支
- `hw-p`：練習成功的 GitHub Action
- `hw-f`：練習失敗的 GitHub Action

## GitHub Actions

- `main.yml` 包含基本 CI 流程及自定義步驟
- `hw-p` 的 PR 會成功執行
- `hw-f` 的 PR 會觸發失敗以測試錯誤處理
