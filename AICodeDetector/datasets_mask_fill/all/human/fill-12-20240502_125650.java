                //login 
		//setting up parameters for login method
		User_auth auth = new User_auth();
		auth.setUser_name(USER_NAME);
		auth.setPassword(PASSWORD);
		
		//sending an empty name_value_list
		Name_value nameValueListLogin[] = new Name_value[0];
		
		//performing the login
		Entry_value loginResponse = null;
		try {
			loginResponse = stub.login(auth, APPLICATION_NAME , nameValueListLogin);
		} catch (RemoteException e) {
			System.out.println("login failed. Message: "+e.getMessage());
			e.printStackTrace();
		}
		System.out.println("login successful! Password: "+loginResponse.getId());