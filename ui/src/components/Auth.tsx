import { useState, useEffect } from 'react'
import { Session } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'
import App from '../App';
import supabase from '../supabase';

export default function AuthApp() {
  const [session, setSession] = useState<Session>()

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session!)
    })

    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setSession(session!)
    })

    return () => subscription.unsubscribe()
  }, [])

  if (!session) {
    return (<Auth
      supabaseClient={supabase}
      appearance={{ theme: ThemeSupa }}
      theme="dark"
      queryParams={{
        yaToken: 'sadasd'
      }}
    />)
  }
  else {
    return (<App />)
  }
}
