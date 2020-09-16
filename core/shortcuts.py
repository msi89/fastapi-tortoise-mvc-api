
password_msg_regex = 'Minimum eight and maximum 20 characters, at least one uppercase letter, one lowercase letter, one number and one special character:'
password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$"


password_light_msg_regex = 'Minimum eight characters, at least one uppercase letter, one lowercase letter and one number:'
password_light_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

email_regex = "^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$"
