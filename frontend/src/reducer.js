import article from './reducers/article';
import articleList from './reducers/articleList';
import auth from './reducers/auth';
import { combineReducers } from 'redux';
import common from './reducers/common';
import editor from './reducers/editor';
import home from './reducers/home';
import contact from './reducers/contact';
import profile from './reducers/profile';
import settings from './reducers/settings';
import {reducer as toastrReducer} from 'react-redux-toastr'
import { routerReducer } from 'react-router-redux';

export default combineReducers({
  article,
  contact,
  articleList,
  auth,
  common,
  editor,
  home,
  profile,
  settings,
  router: routerReducer,
  toastr: toastrReducer
});
