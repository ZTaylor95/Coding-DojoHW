<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
<head>
	<meta charset="ISO-8859-1">
	<title>Omikuji Home Page</title>
	<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
	<!-- For any Bootstrap that uses JS or jQuery-->
	<script src="/webjars/jquery/jquery.min.js"></script>
	<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
</head>
<body>
	<div class="container">
		<h1>Send an Omikuji!</h1>
		<form action="/submit" method="POST" class="form-control">
			<label>Pick any number from 5 to 25</label>
			<input type="number" name="number" id="number" min="5" max="25" class="form-control" />
			<label>Enter the name of a city</label>
			<input type="text" name="city" id="city" class="form-control" />
			<label>Enter the name of any real person</label>
			<input type="text" name="person" id="person" class="form-control" />
			<label>Enter professional endeavor or hobby:</label>
			<input type="text" name="hobby" id="hobby" class="form-control" />
			<label>Enter any type of living thing</label>
			<input type="text" name="thing" id="thing" class="form-control" />
			<label>Say something nice to someone!:</label>
			<input type="text" name="message" id="message" class="form-control" />
			<p>Send and show a friend</p>
			<input type="submit" class="btn btn-success" />
		</form>
	</div>

</body>
</html>