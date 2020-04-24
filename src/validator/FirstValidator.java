/*
 * generated by Xtext 2.20.0
 */
package org.xtext.project.validation;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.eclipse.xtext.validation.Check;
import org.xtext.project.first.AgentSettings;
import org.xtext.project.first.FirstPackage;

/**
 * This class contains custom validation rules. 
 *
 * See https://www.eclipse.org/Xtext/documentation/303_runtime_concepts.html#validation
 */
public class FirstValidator extends AbstractFirstValidator {
	
//	public static final INVALID_NAME = 'invalidName'
//
//	@Check
//	public void checkGreetingStartsWithCapital(Greeting greeting) {
//		if (!Character.isUpperCase(greeting.getName().charAt(0))) {
//			warning("Name should start with a capital",
//					FirstPackage.Literals.GREETING__NAME,
//					INVALID_NAME);
//		}
//	}
	
	@Check
	public void checkLanguageCodeValid(AgentSettings agentP) {
		String patternString = "^[a-z]{2}(-[A-Z]{2})?$";
		Pattern pattern = Pattern.compile(patternString);
		Matcher matcher = pattern.matcher(agentP.getLanguageCode());
		boolean matches = matcher.matches();
		
		if(!matches) {
			error("Language code must be valid (e.g. en-US or da)", FirstPackage.Literals.AGENT_SETTINGS__LANGUAGE_CODE);
		}
	}
	
	@Check
	public void checkTimeZoneValid(AgentSettings agentP) {
		String patternString = "^[a-zA-Z]+/[a-zA-Z]+$";
		Pattern pattern = Pattern.compile(patternString);
		Matcher matcher = pattern.matcher(agentP.getTimeZone());
		boolean matches = matcher.matches();
		
		if(!matches) {
			error("Time zone must be valid (e.g. Europe/Copenhagen)", FirstPackage.Literals.AGENT_SETTINGS__TIME_ZONE);
		}
	}
	
}