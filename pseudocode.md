Register app pseudocode:

      BEGIN
      FUNCTION register
            IF request.method is equal too "POST"
                  username equals GET username FROM  data
                  email equals GET email FROM email data
                  password  equals GET password FROM password data

                  existing_user filters database for username
                  IF username exists
                        SHOW "Username already exists"
                        RETURN back to register page
