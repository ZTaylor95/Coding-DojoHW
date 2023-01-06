<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
         pageEncoding="ISO-8859-1" %>
<!-- c:out ; c:forEach etc. -->
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!-- Formatting (dates) -->
<%@taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<!-- form:form -->
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!-- for rendering errors on PUT routes -->
<%@ page isErrorPage="true" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="ISO-8859-1">
    <title>Display Book</title>
    <!-- for CSS styling-->
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <script type="text/javascript" src="js/app.js"></script>
    <!-- for Bootstrap CSS -->
    <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css"/>
    <!-- For any Bootstrap that uses JS or jQuery-->
    <script src="/webjars/jquery/jquery.min.js"></script>
    <script src="/webjars/bootstrap/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container mt-3">
    <div class="d-flex align-items-center justify-content-between">
        <h1><c:out value="${book.title}"/></h1>
        <a href="/home">back to the book shelves</a>
    </div>
    <div class="mt-5">
        <p><c:out value="${book.creator.userName}"/> read <c:out value="${book.title}"/> by <c:out
                value="${book.author}"/>.</p>
        <p>Here are <c:out value="${book.creator.userName}"/>'s thoughts:</p>
    </div>
    <div>
        <span class="border-top border-4"><c:out value="${book.thoughts}"/></span>
    </div>
    <c:if test="${loggedInUser.id == book.creator.id}">
        <a href="/books/${book.id}/edit">Edit</a>
    </c:if>
</div>
</body>
</html>