"use client";

import { Crisp } from "crisp-sdk-web";
import { useEffect } from "react";



export const CrispChat = () => {
	useEffect(() => {
	  const websiteId = process.env.NEXT_PUBLIC_CRISP_WEBSITE_ID; // Use a NEXT_PUBLIC prefix if using Next.js
	  if (!websiteId) {
		console.error('CRISP_WEBSITE_ID is not set');
		return;
	  }
	  Crisp.configure(websiteId);
	}, []);
  
	return null;
  };

export default CrispChat;
