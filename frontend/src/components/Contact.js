/**
 * More info about react-toasts
 * https://www.npmjs.com/package/react-toasts
 */

import {ToastContainer, ToastStore} from 'react-toasts';
import React from 'react';
import agent from '../agent';
import { connect } from 'react-redux';
import {
  UPDATE_FORM_CONTACT,
  CONTACT,
  CONTACT_PAGE_UNLOADED,
  SUBMIT_WITH_ERRORS,
  REDIRECT_HOME
} from '../constants/actionTypes';

const mapStateToProps = state => ({ ...state.contact });

const mapDispatchToProps = dispatch => ({
  onRedirectToHome: () => 
    dispatch({ type: REDIRECT_HOME }),
  onChangeSubject: value =>
    dispatch({ type: UPDATE_FORM_CONTACT, key: 'subject', value }),
  onChangeMessage: value =>
    dispatch({ type: UPDATE_FORM_CONTACT, key: 'message', value }),
  onChangeEmail: value =>
    dispatch({ type: UPDATE_FORM_CONTACT, key: 'email', value }),
  onSubmit: (username, email, password, errors) => {
    if(errors){
      console.log(errors);
      dispatch({ type: SUBMIT_WITH_ERRORS })
    }else{
      const payload=agent.Contact.sendingFormToBackend(username, email, password);
      dispatch({ type: CONTACT, payload });
    } 
  },
  onUnload: () =>
    dispatch({ type: CONTACT_PAGE_UNLOADED })
});

class Contact extends React.Component {
  constructor() {
    super();
    this.redirectToHome = () => this.props.onRedirectToHome();
    this.changeSubject = ev => this.props.onChangeSubject(ev.target.value);
    this.changeMessage = ev => this.props.onChangeMessage(ev.target.value);
    this.changeEmail = ev => this.props.onChangeEmail(ev.target.value);
    this.submitForm = (subject, email, message, errors) => ev => {
      ev.preventDefault();
      this.props.onSubmit(subject, email, message, errors);
    }
  }

  componentDidMount(){
    this.props.onUnload();
  }
  componentDidUpdate(){
    const success = (!this.props.backendErrors['subject'] && !this.props.backendErrors['email'] && !this.props.backendErrors['message']) && this.props.submitted;
    if(success){
      ToastStore.success('Email was send!', 2000);
      setTimeout(() => {
        this.redirectToHome();
      }, 2000);
    }
  }

  render() {
    const errors = (!this.props.subjectIsValid || !this.props.emailIsValid || !this.props.messageIsValid);
    return (
      <div className="auth-page">
        <div className="container page">
          <div className="row">

            <div className="col-md-6 offset-md-3 col-xs-12">
              <h1 className="text-xs-center">Contact</h1>
              <br></br>

              <form onSubmit={this.submitForm(this.props.subject, this.props.email, this.props.message, errors)}>
                <fieldset>
                <p hidden={(!this.props.submittedAtLeastOnce ||  !this.props.subjectIsValid) || !this.props.backendErrors['subject']} ><font size="3" color="red">You have not introduced a subject!</font></p>
                <p hidden={!this.props.submittedAtLeastOnce ||  this.props.subjectIsValid} ><font size="3" color="red">You have not introduced a subject!</font></p>
                  <fieldset className="form-group">
                    <input
                      className="form-control form-control-lg"
                      type="text"
                      placeholder="Subject"
                      value={this.props.subject}
                      onChange={this.changeSubject} />
                  </fieldset>
                  <p hidden={(!this.props.submittedAtLeastOnce || !this.props.emailIsValid) || !this.props.backendErrors['email']} ><font size="3" color="red">You have not introduced a valid email!</font></p>
                  <p hidden={!this.props.submittedAtLeastOnce || this.props.emailIsValid } ><font size="3" color="red">You have not introduced a valid email!</font></p>
                  <fieldset className="form-group">
                    <input
                      className="form-control form-control-lg"
                      type="email"
                      placeholder="Email"
                      value={this.props.email}
                      onChange={this.changeEmail}
                       />
                  </fieldset>
                  <p hidden={(!this.props.submittedAtLeastOnce || !this.props.messageIsValid) || !this.props.backendErrors['message']} ><font size="3" color="red">Messages have to have at least 20 characters!</font></p>
                  <p hidden={!this.props.submittedAtLeastOnce || this.props.messageIsValid} ><font size="3" color="red">Messages have to have at least 20 characters!</font></p>
                  <fieldset className="form-group">
                    <textarea
                      className="form-control form-control-lg"
                      placeholder="Message"
                      value={this.props.message}
                      onChange={this.changeMessage} />
                  </fieldset>

                  <button
                    className="btn btn-lg btn-primary pull-xs-right"
                    type="submit"
                    disabled={(errors && this.props.submittedAtLeastOnce) || (this.props.submitting || this.props.submitted)}>
                    Send!
                  </button>
                  <ToastContainer position={ToastContainer.POSITION.TOP_RIGHT} store={ToastStore}/>
                </fieldset>
              </form>
            </div>

          </div>
        </div>
      </div>
    );
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Contact);