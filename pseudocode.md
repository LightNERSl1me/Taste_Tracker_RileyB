### Register app pseudocode:

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
      END


### App.js service worker pseudocode:
      
      BEGIN
            IF service worker in vavigator:
                  RUN service worker file
                        IF service worker OUTPUT workes:
                              continue running
                        ELSE service worker OUTPUT error:
                              DIPSLAY Service wprler registratiom failed
      END

### Review list

      BEGIN
            IF reviews avalable
            FORMAT class for reviews
                  Resteraunt name OUTPUT from review
                  Resteraunt Rating OUTPUT from review
                  Date made OUTPUT from review

                  FORMAT class review text from review
                  FORMAT review author from review

      END              
                  
                  
