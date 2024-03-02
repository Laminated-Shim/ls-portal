/*
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
*/

import React, { useState } from 'react';

const tabs = [
  { name: 'Jobs', href: '#', current: true },
  { name: 'Quotes', href: '#', current: false },
  { name: 'Sales', href: '#', current: false },
]

function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}


export default function Example(props) {
  const { onTabChange } = props;
  const [activeTab, setActiveTab] = useState(tabs[0]);
  return (
    <div>
      <div className="sm:hidden">
        <label htmlFor="tabs" className="sr-only">
          Select a tab
        </label>
        {/* Use an "onChange" listener to redirect the user to the selected tab URL. */}
        <select
          id="tabs"
          name="tabs"
          className="block w-full rounded-md border-gray-300 focus:border-indigo-500 focus:ring-indigo-500"
          defaultValue={tabs.find((tab) => tab.current).name}
        >
          {tabs.map((tab) => (
            <option key={tab.name}>{tab.name}</option>
          ))}
        </select>
      </div>
      <div className="hidden sm:block">
        <nav className="flex space-x-4" aria-label="Tabs">
          {tabs.map((tab) => (
            <button
              key={tab.name}
              className={classNames(
                tab == activeTab ? 'button bg-gray-100 text-gray-700' : 'button text-gray-500 hover:text-gray-700',
                'rounded-md px-3 py-2 text-sm font-medium'
              )}
              aria-current={tab.current ? 'page' : undefined}
              onClick={ ()=> {
                onTabChange(tab.name);
                setActiveTab(tab)
              }}
            >
              {tab.name}
            </button>
          ))}
        </nav>       
      </div>
    </div>
  )
}
