import logo from './logo.svg';
import './App.css';

import { TonConnectUIProvider } from '@tonconnect/ui-react';
import { TonConnectButton } from '@tonconnect/ui-react';

function App() {
    return (
        <TonConnectUIProvider manifestUrl="https://raw.githubusercontent.com/Vladikasik/TON-streams/js-way/tonconnect-manifest.json">
             <Header />
        </TonConnectUIProvider>
    );
}

export const Header = () => {
  return (
      <header>
          <span>My App with React UI</span>
          <TonConnectButton />
      </header>
  );
};

export default App;
