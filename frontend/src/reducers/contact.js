import {
	UPDATE_FORM_CONTACT,
	CONTACT,
	CONTACT_PAGE_UNLOADED,
	ASYNC_START,
	ASYNC_END,
	SUBMIT_WITH_ERRORS
} from "../constants/actionTypes";

const backendErr = {"message":false, "email":false, "subject":false};

const INITIAL_STATE = {
	submitting: false,
	success: false,
	error: false,
	open: false,
	message: "",
	email: "",
	subject:"",
	emailIsValid:false,
	subjectIsValid:false,
	messageIsValid:false,
	submittedAtLeastOnce:false,
	backendErrors:backendErr,
	submitted:false
};
const validate = "IsValid";

export default function(state = INITIAL_STATE, action) {
	switch (action.type) {
		case SUBMIT_WITH_ERRORS:
			return { ...state,
				submittedAtLeastOnce:true };
		case UPDATE_FORM_CONTACT:
			switch(action.key){
				
				case "email":
					let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
					action.validate = re.test(String(action.value).toLowerCase());
					break;
				
				case "message":
					action.value.length >= 20? action.validate = true : action.validate = false;
					break;
				
				case "subject":
					action.value.length > 0? action.validate = true : action.validate = false;
					break;
				default:
					return ;
			}
			return { ...state,
				 [action.key]: action.value,
				 [action.key+validate]: action.validate,
				backendErrors:backendErr,
				submitted:false};
		case CONTACT:
			return {
				...state,
				backendErrors: action.payload.errors? action.payload.errors : backendErr,
				submitted:true};

		case ASYNC_START:
			if (action.subtype === CONTACT) {
				return { ...state, submitting: true,
					submittedAtLeastOnce:true };
			}
			return {...state};

		case ASYNC_END:
			return { ...state, submitting: false };

		case CONTACT_PAGE_UNLOADED:
			  return INITIAL_STATE;
			  
		default:
			return state;
	}
}