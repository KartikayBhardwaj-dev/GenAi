# genAi-week03
# Calling LLM api via python
## Two ways Direct Api or Framework(langchain) so calling it through means f(x) = maybe y / maybe error / maybe slow / maybe weird output
# Retry Logic
## Api fails randomly 500 error, timeout, rate limit w/o retry App crashes with retry Try → Fail → Retry → Success
# Timeout Handling
## Api hangs : set timeout = 30 sec after 30 sec kill requests
# Logging
## w/o logging we only know "Something Broken "
## with logging: Prompt → Response → Error → Timestamp ✅
# Json Enforcement: 
## means we structure output as different JSOn outputs : Zero-shot, few-shot , strict-json generator