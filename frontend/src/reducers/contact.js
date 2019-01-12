import {
	UPDATE_FORM_CONTACT,
	EMAIL,
	CONTACT_PAGE_UNLOADED,
	ASYNC_START,
	ASYNC_END,
	SEND
} from "../constants/actionTypes";

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
	submittedAtLeastOnce:false
};
const validate = "IsValid";

export default function(state = INITIAL_STATE, action) {
	switch (action.type) {
		case SEND:
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
				 [action.key+validate]: action.validate};
		case EMAIL:
			return { ...state};

		case ASYNC_START:
			if (action.subtype === EMAIL) {
				return { ...state, submitting: true,
					submittedAtLeastOnce:true };
			}
			break;

		case ASYNC_END:
			return { ...state, submitting: false };

		case CONTACT_PAGE_UNLOADED:
			  return {};
			  
		default:
			return state;
	}
}