# AI Company: your automated "employees"

Four scripts that run on a schedule, each doing one job for your digital-product business:

| Employee | Job | Schedule (UTC) |
|---|---|---|
| Creator | Drafts a new product + store listing | Mondays 07:00 |
| Marketer | 5 social posts + 1 article outline | Daily 08:00 |
| Support | Drafts replies to messages in `support/inbox.txt` | Daily 09:00 |
| Analyst | Reads `data/sales.csv`, recommends next steps | Sundays 10:00 |

**They never publish anything themselves.** Every draft is sent to your Telegram and saved in the `queue/` folder. You review it and post it yourself.

## Setup (about 30 minutes)

### 1. Get an Anthropic API key
Go to console.anthropic.com, add about $10 credit, create an API key, and copy it.

### 2. Create a Telegram bot (optional but recommended)
1. In Telegram, message **@BotFather**, send `/newbot`, follow the steps, and copy the **token**.
2. Send any message to your new bot.
3. Open `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` in your browser and find `"chat":{"id":123456789`. That number is your **chat id**.

### 3. Create the GitHub repo
1. Sign up at github.com.
2. Click **+** (top right) -> **New repository**. Name it `ai-company`, choose **Private**, click **Create**.
3. Click **uploading an existing file**, unzip this project on your computer, and drag **everything inside the folder** into the page. Make sure the `.github` folder is included (it is hidden on Mac: press Cmd+Shift+. in Finder to see it).
4. Click **Commit changes**.

### 4. Add your secrets
Repo -> **Settings** -> **Secrets and variables** -> **Actions** -> **New repository secret**. Add:
- `ANTHROPIC_API_KEY`
- `TELEGRAM_TOKEN` (if using Telegram)
- `TELEGRAM_CHAT_ID` (if using Telegram)

Never put keys in the code files.

### 5. Set your niche
Same page -> **Variables** tab -> **New repository variable**: name `NICHE`, value e.g. `budget planners for university students`. (If you skip this, it uses a default.)

### 6. Allow the employees to save drafts
Repo -> **Settings** -> **Actions** -> **General** -> scroll to **Workflow permissions** -> choose **Read and write permissions** -> **Save**.

### 7. Test it
Repo -> **Actions** tab -> click **creator** on the left -> **Run workflow**. After about a minute you should get a Telegram message and a new file in the `queue/` folder. If something fails, click the run to see the error and send it to me.

## Using the employees
- **Support:** paste customer messages into `support/inbox.txt` (separate with `---`) and fill in `support/faq.txt` with your real policies.
- **Analyst:** paste your sales export from Stripe/Gumroad into `data/sales.csv`.
- **Costs:** roughly $5-30/month in API usage. To save money, edit the schedules in `.github/workflows/` (e.g. change the marketer from daily to weekly).

## Rules to stay safe
No fake reviews or testimonials, disclose affiliate links, and check each platform's rules on AI-generated content. Read every draft before you post it.
