import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import React from 'react';
import ReduxToastr from 'react-redux-toastr'
import { store, history} from './store';
import { Route, Switch } from 'react-router-dom';
import { ConnectedRouter } from 'react-router-redux';

import App from './components/App';

ReactDOM.render((
  <Provider store={store}>
    <div>
    <ConnectedRouter history={history}>
        <Switch>
          <Route path="/" component={App} />
        </Switch>
      </ConnectedRouter>
      <ReduxToastr
        timeOut={4000}
        newestOnTop={false}
        preventDuplicates
        position="top-right"
        progressBar
        closeOnToastrClick/>
    </div>
  </Provider>

), document.getElementById('root'));
